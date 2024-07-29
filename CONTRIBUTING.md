# Contributing

## Development

### Fixtures

To export fixtures for the blog app, run the following command:

```bash
python manage.py dumpdata --natural-foreign --indent 2 -e contenttypes -e auth.permission -e wagtailcore.groupcollectionpermission     -e wagtailcore.grouppagepermission -e wagtailimages.rendition -e sessions -e wagtail_vector_index.embedding  > fixtures_data.json
```

To load fixtures, run the following command:

```bash
python manage.py loaddata fixtures_data.json
```