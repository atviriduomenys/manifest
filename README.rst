.. default-role:: literal

Lithuanian open government data repository
##########################################

This is the place where you can request data for you project or describe data
collected by Lithuanian government.


What's it all about?
====================

Currently Lithuaniang government is working on open data project and opening
data. The idea of this repository is to help gevernment decide what data to
open first and how to transform data so that final result would be as close as
posible to what is needed for open data users.

Without knowing by who, how it will be used and what data is needed there are
number of issues:

- Priorities of what to open first are not clear.

- It is not clear what transformations are needed to best meet the demand.

- What economical or social implact opened data will do.

In other words, without clearly knowing what is needed, it is eassy to open
datasets, that will never be used in practice. And that would be waste of time
and effort.

So tell us, what data you need and hopefully government will do their best to
give you exactly what you need.


How to submit request for data?
===============================

Requests for data are submitted as `GitHub pull requests`_. One pull request
should describe data needed for a project in YAML_ format.

YAML_ files are organized like this::

  schema/
    <object>.yml
  providers/
    <provider>.yml
  sources/
    <provider>/
      <source>.yml
  projects/
    <project>.yml
  media/
    providers/
      <provider>/
        logo.png
    projects/
      <project>/
        logo.png

First, in order for eveyone to speek the same vocabulary, all object and field
names must be defined in `schema/` folder. This will help to connect things.

Schema should looks like this:

.. code-block:: yaml

  # schema/seimo_narys.yml
  id: "seimo_narys"
  title: "Member of Parliament"
  description: ""
  type: "schema"
  properties:
    first_name:
      title: "First name"
      type: "string"
    last_name:
      title: "Last name"
      type: "string"

As you can see it looks a bit similar to json-schema_, so meaning of some
fields are well defined in json-schema_ specifications.

If you already know the source of data needed for youu project, you can include
that information too:

.. code-block:: yaml

  # sources/lrs/ad.yml
  id: "lrs/ad"
  title: "Members of Parliament (XML)"
  description: "XML file containing data about members of parliament."
  type: "source"
  source:
    - "http://apps.lrs.lt/sip/p2b.ad_seimo_nariai"
    - "xml:"
  provider: "lrs"
  objects:
    seimo_narys:
      source: "xpath:/SeimoInformacija/SeimoKadencija/SeimoNarys"
      properties:
        first_name:
          type: "string"
          source: "xpath:@vardas"
        last_name:
          type: "string"
          source: "xpath:@pavardė"

Defining a source is the most complicated thing, but you don't have to define
exact location of the data, `source` parameter is optional. Here I just wanted
to demonstrate complete example of how this can look.

The idea with sources, is that you can exactly specify data location, so that
data can be extracted automatically. Also, source definition can be validated
automatically by checking if defined data are really there.

But in most cases we will not have direct access to data, so that's why
`source` parameter is optional. It is enough to just specify a URL and list
properties that we think are provided by the source.

Also provider `lrs` must be defined too:

.. code-block:: yaml

  # providers/lrs.yml
  id: "lrs"
  title: "Lietuvos Respublikos Seimas"
  type: "provider"
  logo: "logo.png"


Last thing, which could be second thing after schema if source is ommited, is
project file. Here is an example:

.. code-block:: yaml

  # projects/manopozicija.lt.yml
  id: "projects/manopozicija.lt"
  title: "ManoPozicija.lt"
  type: "project"
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
          type: "string"
          source: "sources/lrs/ad"
        last_name:
          type: "string"
          source: "sources/lrs/ad"

Here `source` has a bit different meaning, it just mapps to the source scheme
and tells, that this project uses data from that specified source. While in
source definition, `source` parameter specifies exact location of data.

Another property `impact` provides data about social and economical impact. Bot
future and past dates can be provided for estimated and retrospective impact.
This parameter helps to prioritize what data needs to be opened first. Projects
with a higher impact should be supplied with the data first.

That is it.

Once pull request is created, automated scripts will check if everything is OK,
then a human will review pull request and if everything is OK, then pull
request will be accepted.

If you don't know how to use git and don't know YAML_, then you can simply
`create a task`_ and if your project idea will be worth addeng, then someone alse
will take care of describing you data needs in machine readable format as
explained above.


.. _GitHub pull requests: https://help.github.com/articles/creating-a-pull-request/
.. _YAML: https://en.wikipedia.org/wiki/YAML
.. _json-schema: https://en.wikipedia.org/wiki/JSON#JSON_Schema
.. _create a task: https://github.com/sirex/opendata/issues/new
