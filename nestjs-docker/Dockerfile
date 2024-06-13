FROM node:20-alpine As base

RUN npm i -g pnpm

# BUILD FOR LOCAL DEVELOPMENT
FROM base As development

# Create app directory
WORKDIR /usr/src/app

# Copy application dependency manifests to the container image.
# A wildcard is used to ensure copying both package.json AND pnpm-lock.yaml (when available).
# Copying this first prevents re-running npm install on every code change.
COPY --chown=node:node package.json pnpm-lock.yaml ./

# Install app dependencies
RUN pnpm install

# Bundle app source
COPY --chown=node:node . .

# Use the node user from the image (instead of the root user)
USER node

# BUILD FOR PRODUCTION
FROM base As build

# Create app directory
WORKDIR /usr/src/app

COPY --chown=node:node package.json pnpm-lock.yaml ./

# To run `npm run build` we need access to the Nest CLI which is a dev dependency. In the previous development stage we ran `npm ci` which installed all dependencies, so we can copy over the node_modules directory from the development image
COPY --chown=node:node --from=development /usr/src/app/node_modules ./node_modules

COPY --chown=node:node . .

# Run the build command which creates the production bundle
RUN pnpm build
RUN pnpm prune --prod

# Set NODE_ENV environment variable
ENV NODE_ENV production

# Remove husky from the production build and install the production dependencies
RUN pnpm install --frozen-lockfile

USER node

# Migration
FROM build As migration

# Create app directory
WORKDIR /usr/src/app

# Run the migration command
CMD [ "npm", "migrate:run" ]

# PRODUCTION
FROM base As production

# Create app directory
WORKDIR /usr/src/app

# Copy the bundled code from the build stage to the production image
COPY --chown=node:node --from=build /usr/src/app/node_modules ./node_modules
COPY --chown=node:node --from=build /usr/src/app/dist ./dist

ENV NODE_ENV production

# Start the server using the production build
CMD [ "node", "dist/main.js" ]
