#base image
FROM node:25-alpine

#Work Directory
WORKDIR /app

#copy to work dir
COPY package.json package.json
COPY app.js app.js

#install dependancy
RUN npm install

#expose port
EXPOSE 3000

#CMD
CMD ["npm", "start"]
