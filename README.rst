.. default-role:: literal

.. image:: https://gitlab.com/atviriduomenys/manifest/badges/master/pipeline.svg
   :target: https://gitlab.com/atviriduomenys/manifest/commits/master


Lithuanian Open Data Manifest
#############################

Here you can request data for your project or tell what data your project
already use and how things are going for the project.

This is a non-official community effort. There is no guarantee that requested
data will ever be opened. But knowing what data are needed is important.


What's it all about?
====================

Currently Lithuanian government is working on a open data project. The idea of
this repository is to help government decide what data to open first and how to
transform data so that final result would be as close as posible to what is
needed for data users.

Without knowing who is going to use the data, how it will be used and what data
is needed, there are number of issues:

- Priorities of what to open first are not clear.

- It is not clear what transformations are needed to best meet the demand.

- What economical or social implact opened data will do.

In other words, without clearly knowing what data users need, it is eassy to
open datasets, that will never be used in practice. And that would be waste of
time and effort.

So please tell us, what data you need and hopefully government will do their
best to give you exactly what you need. Wouldn't it be great?


How to submit request for data?
===============================

Requests for data are submitted as `GitHub pull requests`_. One pull request
should describe data needed for a project in YAML_ format.

YAML_ files are organized into this structure::

  manifest/
    models/
      <object>.yml
    owners/
      <owner>.yml
    datasets/
      <owner>/
        <dataset>.yml
    projects/
      <project>.yml
    media/
      owners/
        <owner>/
          logo.png
      projects/
        <project>/
          logo.png


Here is an example, how a project could request the data:

.. code-block:: yaml

  # projects/manopozicija.lt.yml
  ---
  name: "projects/manopozicija.lt"
  title: "ManoPozicija.lt"
  type: "project"
  verson: 1
  date: "2019-01-06"
  impact:
    - {year: 2015, users: 10, revenue: 0, employees: 0}
    - {year: 2016, users:  0, revenue: 0, employees: 0}
    - {year: 2017, users:  0, revenue: 0, employees: 0}
    - {year: 2018, users: 10, revenue: 0, employees: 0}
    - {year: 2019, users: 20, revenue: 0, employees: 0}
  objects:
    seimo_narys:
      properties:
        first_name:
        last_name:

`impact` parameter is used to describe social and economical impact. Both
future and past dates can be provided for estimated and retrospective impact.
This parameter helps to prioritize what data needs to be opened first. Projects
with a higher impact should be supplied with the data first.


What is the purpose of data models?
===================================

It is very likely that many projects will use same data properties. In order to
know how many projects use the same data properties, all data properties are
defined in one places called models.

Here is example how model file looks:

.. code-block:: yaml

  # models/seimo_narys.yml
  ---
  name: seimo_narys
  title: "Member of Parliament"
  type: model
  verson: 1
  date: 2019-01-06
  properties:
    first_name:
      title: "First name"
      type: string
    last_name:
      title: "Last name"
      type: string

All object and property names must be defined in model file, before using
those names in data or source files.


Datasets
========

Datasets are used to descripe external data sources, here is an example:

.. code-block:: yaml

  ---
  name: gov/lrs/ad
  type: dataset
  verson: 1
  date: 2019-01-06
  resources:
    frakcijos:
      type: xml
      source: http://apps.lrs.lt/sip/p2b.ad_seimo_frakcijos
      objects:
        politika/seimas/pareigos:
          source: /SeimoInformacija/SeimoKadencija/SeimoFrakcija/SeimoFrakcijosNarys
          properties:
            grupes_rusis:
              prepare: "'politika/seimas/frakcija'"
            grupe:
              source: ../@padalinio_id
    komitetai:
      type: xml
      source: http://apps.lrs.lt/sip/p2b.ad_seimo_komitetai
      objects:
        politika/seimas/pareigos:
          source: /SeimoInformacija/SeimoKadencija/SeimoKomitetas/SeimoKomitetoNarys
          properties:
            grupes_rusis:
              prepare: "'politika/seimas/grupė'"
            grupe:
              source: ../@padalinio_id

Here we have a dataset with two resources, each resource is mapped to the same
object called `politika/seimas/pareigos`.


Another example:

.. code-block:: yaml

  # datasets/gov/lrs/ad.yml
  name: gov/lrs/ad
  title: "Members of Parliament (XML)"
  description: "XML file containing data about members of parliament."
  type: dataset
  verson: 1
  date: "2019-01-06"
  website: https://www.lrs.lt/sip/portal.show?p_r=15818&p_k=1
  owner: gov/lrs
  resources:
    seimas:
      type: xml
      source: http://apps.lrs.lt/sip/p2b.ad_seimo_nariai
      objects:
        seimo_narys:
          source: /SeimoInformacija/SeimoKadencija/SeimoNarys
          properties:
            first_name:
              source: "@vardas"
            last_name:
              source: "@pavardė"

The idea with sources, is that you can specify exact location of the data. Just
by using descriptions provided in `source` fields, data can be extracted in a
fully automated way. Well at least the simple cases. In addition this detailed
source description can be used to validate if source data are really there.

`gov/lrs` parameter points to another YAML file where owner is defined. Here
is how this file looks:

.. code-block:: yaml

  # owners/gov/lrs.yml
  name: gov/lrs
  title: "Lietuvos Respublikos Seimas"
  type: owner
  logo: logo.png

`logo` property here points to `media/owners/gov/lrs/logo.png` file.


I don't know how to create a pull request
=========================================

If you don't know how to use git and don't know YAML_, then you can simply
`create a task`_ and if your project idea will be worth adding, then someone
alse will take care of describing you data needs in machine readable format as
explained above.


Automated checks
================

Once pull request is created, automated scripts will check if everything is OK,
then a human will review pull request and if everything is OK, then pull
request will be accepted.

If you want to check yaml files locally, you can run this command::

  make check


Data sources
============

Here I will try to explain, how `source` parameter works.

`source` parameter can be defined in three different places:

.. code-block:: yaml

  resources:
    resource:
      type:
      source: # resource scope
      objects:
        object:
          source: # object scope
          properties:
            prop:
              source: # property scope


XML source
----------

.. code-block:: yaml

  resources:
    resource:
      type: xml
      source: https://example.com/data.xml
      objects:
        object:
          source: /object
          properties:
            field:
              source: @attribute


JSON source
-----------

.. code-block:: yaml

  resources:
    resource:
      type: json
      source: https://example.com/items.json
      objects:
        object:
          source: "items"
          properties:
            id:
              source: "id"


PostgreSQL source
-----------------

.. code-block:: yaml

  resources:
    resource:
      type: sql
      source: postgresql://localhost/dbname
      objects:
        object:
          source: tablename
          properties:
            field:
              source: fieldname

Another example with a query:

.. code-block:: yaml

  resources:
    resource:
      type: sql
      source: postgresql://localhost/dbname
      objects:
        object:
          source: >
            SELECT *
            FROM table1
            JOIN table2 ON (table1.id = table2.id)
            WHERE table1.param > 42
            ORDER BY table2.param
          properties:
            field:
              source: fieldname


HTML table source
-----------------

.. code-block:: yaml

  resources:
    resource:
      type: htmltable
      source: https://example.com/some/page.html
      objects:
        object:
          source: css querylto .table
          properties:
            field:
              source: "Some column name"


OpenDocument Spreadsheet
------------------------

.. code-block:: yaml

  resources:
    resource:
      type: ods
      source: https://example.com/data.ods
      objects:
        object:
          source: SheetNam"
          properties:
            field:
              source: A


.. _GitHub pull requests: https://help.github.com/articles/creating-a-pull-request/
.. _YAML: https://en.wikipedia.org/wiki/YAML
.. _json-schema: https://en.wikipedia.org/wiki/JSON#JSON_Schema
.. _create a task: https://github.com/sirex/opendata/issues/new


Data types
==========

ref
---

You can specify foreign key relations using `ref` type:

.. code-block:: yaml

  name: politika/seimas/kontaktai
  type: model
  properties:
    id: {type: pk}
    seimo_narys:
      type: ref
      object: politika/seimas/seimo_narys

Here `seimo_narys` points to `politika/seimas/seimo_narys`, key refers to
`politika/seimas/seimo_narys` primary key, which is specified by `pk` type.

backref
-------

It is also possible to specify back reference which is list of all objects
referring to this one. Here is an example:

.. code-block:: yaml

  name: politika/seimas/seimo_narys
  type: model
  properties:
    id:
      type: pk
    kontaktai:
      type: backref
      object: politika/seimas/kontaktai
      property: seimo_narys


In order to create many to many relation you need to add `secondary` parameter.
This parameter can be `true` or name of secondary object through which relation
is created. `secondary` is `true` then secondary table will be created
automatically.


generic
-------

Generic type allows to specify a reference to an object without specifying one
object time. You can refer to any obect type.

In models you define it like this:

.. code-block:: yaml

   name: politika/seimas/pareigos
   type: model
   properties:
      grupė:
         type: generic
         enum:
           - politika/seimas/grupė
           - politika/seimas/frakcija
           - politika/partija

Here `grupė` is a generic field which points to one of 3 specified object
types. Under the hood data is stored using two virtual properties `id` and
`object`. You can specify virtual properties like this:

.. code-block:: yaml

   name: gov/lrs/ad
   type: dataset
   resources:
     resource:
       type: xml
       objects:
          politika/seimas/pareigos:
            properties:
              grupes_rusis:
                prepare: "'politika/seimas/frakcija'"
              grupe:
                source: ../@padalinio_id


Versioning
==========

Vocabularies, datasets and projects are all versioned. All these objects must
have `version` and `date` parameters. `versions` tells version number and
`date` tells when this version was released.

All mentioned object YAML files are interpreted as lists. First list item
represent current and first version. For example:

.. code-block:: yaml

  ---
  name: gov/lrs/ad
  title: "Members of Parliament (XML)"
  type: dataset
  version: 1
  date: "2019-01-06"
  owner: gov/lrs
  resources:
    resource:
      type: xml
      source: http://apps.lrs.lt/sip/p2b.ad_seimo_nariai
      objects:
        politika/seimas/seimo_narys:
          source: /SeimoInformacija/SeimoKadencija/SeimoNarys
          properties:
            id:
              source: "@asmens_id"
            vardas:
              type: string
              source: "@vardas"

Now in order to add new version you need to add new version entry and also
update the first version, since first version is also a current version:

.. code-block:: yaml

  ---
  name: gov/lrs/ad
  title: "Members of Parliament (XML)"
  type: dataset
  version: 1
  date: "2019-01-06"
  owner: gov/lrs
  resources:
    resource:
      type: xml
      source: http://apps.lrs.lt/sip/p2b.ad_seimo_nariai
      objects:
        politika/seimas/seimo_narys:
          source: /SeimoInformacija/SeimoKadencija/SeimoNarys
          properties:
            id:
              source: @asmens_id
            vardas:
              type: string
              source: @vardas
            pavardė:
              type: string
              source: @pavardė
              version: 2
  ---
  version: 2
  date: "2019-01-07"
  resources:
    resource:
      objects:
        politika/seimas/seimo_narys:
          properties:
            pavardė:
              type: string
              source: @pavardė

Now we know what current version is and that `pavardė` was added on version
`2`, we can always look at the version `2` antree to find release date.

All objects in first version without `version` parameter melongs to first
version.

All version entries have the same schema as first entry, except all new
versions are merged into current version and then schame validation is applied.


Flags
=====

:unreadable:

   Data is machine unreadable. For example, instead of coordinates a plain text
   address is given.

:licence:

   Licence is not suitable for open data.

:fragments:

   Data provided through an API and there is no way to download all data at
   once. For example, first you have to get list of elections, then go to each
   election and get election tour, then from each tour get election district
   and so on. You should be able to get all districts at once.

:noref:

   A property does not have a reference to another object, instead of reference
   a textual representation of an object is given.

:denorm:

   A property is denormalized. For example, instead given reference to an
   object, multiple properties are included within another object.

:aggregated:

   Data values are aggregated.

:derived:

   Data values are derived from other values.

:noenum:

   Fixed list of possible values is not provided.

:nolink:

   No direct link to data. For example, one has to fill in a form or be logged
   in to get data.
