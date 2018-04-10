# Rancher Manager
mange rancher services via rancher API ([v2-beta](http://rancher.com/docs/rancher/v1.6/en/api/v2-beta/))

## Feature
- [Upgrade services](http://rancher.com/docs/rancher/v1.6/en/api/v2-beta/api-resources/service/#upgrade) via yaml configuration 
- Generate YAML confgiuration of container ID
- Push YAML configuration to git repository for CI flow

### How to run
Have to change 3 configuration which is
- rancher_list_to_yaml.yaml (list of rancher that would like to generate to yaml)
- rancher_service_to_update.yaml (list of rancher services that would like to upgrade)
- rancher_request.py (for setting secret key and rancher server)

then run

```python rancher_manager.py UPGRADE```

### Limitation
- Upgrade services to latest image based on same image
