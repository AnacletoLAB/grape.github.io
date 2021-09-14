# grape-ui

## Project setup
```sh
yarn install
```

### Compiles and hot-reloads for development
```sh
yarn serve
```

### Compiles and minifies for production
```sh
yarn build
```

### Lints and fixes files
```sh
yarn lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

## How to deploy

Edit config.ts (remember to add the /api at the end)
```sh
yarn
# Edit config.ts by setting backend's address
yarn build
# You can find the build in ./dist .
# Move its content to /var/www/html or wherever you host it
```
