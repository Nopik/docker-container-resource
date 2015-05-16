# Concourse CI resource for Docker container management

Already usable, but still work in progress.

# TODO:

- add better support for ports configuration

# Example:

```
resources:
- name: docker
  type: docker-container
  source:
    host: https://192.168.59.103:2376
    name: my-container-name
    image: redis
    tls: 1
    certs:
      ca: {{ca-pem}}
      cert: {{cert-pem}}
      key: {{key-pem}}

jobs:
- name: test-docker-container
  public: true
  plan:
   - put: docker
     params:
       cmd: run
       ports:
         "7000": 7001
         "6000": 6001
       volumes:
         "/host-path":
           bind: /container-path
       volumes_from:
         - other-container
   - get: docker
     trigger: false
   - task: dump
     config:
       platform: linux
       image: docker:///ubuntu#14.04
       inputs:
        - name: docker
       run:
         path: cat
         args: [docker/inspect]
```


