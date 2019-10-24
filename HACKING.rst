.. default-role:: literal

Pushin data from one Spinta to another
======================================

I will call *source* a Spinta instance from which data will be collected and
*target* another Spinta instance where data will be written.

On *target* spinta create client::

    env/bin/spinta client add

And add all needed scopes, by editin client file::

    vim config/clients/client.yml

::

    client_id: client
    client_secret_hash: pbkdf2$sha256$756147$TPNDgs2d0rOCSfx0mkeSPw$13lA-ssnH3Jo5L0G-0VIPCln5tBkoLdRnoSfqmXpaOM
    scopes:
      - spinta_set_meta_fields
      - spinta_insert
      - spinta_upsert
      - spinta_update
      - spinta_delete
      - spinta_getone
      - spinta_getall
      - spinta_search
      - spinta_changes

Restart *target* Spinta::

    sudo systemctl restart spinta

On *source* Spinta, create credentials file::

    [client@atviriduomenys.lt]
    client_id = client
    client_secret = secret
    scopes =
      spinta_set_meta_fields
      spinta_insert
      spinta_upsert
      spinta_update
      spinta_delete
      spinta_getone
      spinta_getall
      spinta_search
      spinta_changes

And then run the `push` command::

    env/bin/spinta push -r ../credentials.cfg -c client -d gov/lrs/xml https://atviriduomenys.lt/

To update *source* data from external sources run::

    env/bin/spinta pull gov/lrs/xml --push
