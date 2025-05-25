# Stage 1: Build the React application
FROM node:18-alpine AS build-stage

WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock)
COPY package.json package-lock.json* ./
# npm ci is generally recommended for CI/CD environments as it uses package-lock.json strictly
# and can be faster. Using npm install for broader compatibility here.
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the application
RUN npm run build

# Stage 2: Serve the application with Nginx
FROM nginx:alpine

# Copy the build output from the build stage to Nginx's web root directory
COPY --from=build-stage /app/build /usr/share/nginx/html

# Copy the Nginx configuration file
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# Command to run Nginx (default command for nginx:alpine is usually sufficient)
# CMD ["nginx", "-g", "daemon off;"] # This is often the default
