FROM node:25-alpine3.22 as builder
WORKDIR /app
COPY package*.json /app/
RUN npm ci
COPY . .
RUN npm run build


FROM nginx:1.29.4-alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/*.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
