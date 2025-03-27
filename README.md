<h1 align="center">
  URL-Shortner
</h1>


## Technologies

- ### Back end

  - [Express](https://expressjs.com/)- Nodejs framwork for building the REST Apis
  - [Mongodb](http://mongodb.com/)- Document oriented NoSQL database
  - [Mongoose](https://http://mongoosejs.com)- MongoDB object modeling tool
  - [Short-id](https://github.com/dylang/shortid)- Short id generator
  - [Valid-url](https://github.com/ogt/valid-url)- URI validation functions
  - [Nginx](https://www.nginx.com)- Nginx is event-based and asynchronous web server.

- ### Front end

  - [React](https://reactjs.org/) - JavaScript library for building user interfaces.
  - [React-router](https://github.com/ReactTraining/react-router)- Complete routing library for React
  - [Materialize css](http://materializecss.com/)- Responsive front-end framework based on Material Design

## Getting Started

#### Clone the project

```sh
# clone it
git clone https://github.com/muhzi4u/URL-Shortner.git
cd URL-Shortner
# Make it your own
rm -rf .git && git init
```

#### Run back end

```
# Move to server folder
cd server/
# Install dependencies
yarn install

# Start  server
yarn run server
```

#### Run front end

```
# Move to client folder
cd client/
# Install dependencies
yarn install
# Start  client
yarn run start
```

## Demo

![NSGIF](https://j.gifs.com/1rnQV0.gif)

## Blog

[Creating custom URL shortener with Nodejs](https://codeburst.io/creating-custom-url-shortener-with-nodejs-de10bbbb89c7)

## ☑ TODO

- [x] Front end app
- [x] Documentation and Blog
- [x] Add Redis for caching
- [ ] Change short code algorithm and check duplicate short codes

## License

MIT
