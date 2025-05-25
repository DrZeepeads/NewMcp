# Use an official Node.js runtime as a parent image
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json (or yarn.lock if you use yarn)
# to leverage Docker cache
COPY package.json package-lock.json* ./

# Install dependencies
# Using npm ci for potentially faster and more reliable builds in CI/CD,
# but npm install is also fine. --omit=dev to skip development dependencies.
RUN npm ci --omit=dev

# Bundle app source
COPY . .

# The MCP server in index.js defaults to port 3001 if MCP_PORT is not set.
# Expose the port the app runs on
EXPOSE 3001

# Define the command to run the application
CMD [ "node", "index.js" ]
