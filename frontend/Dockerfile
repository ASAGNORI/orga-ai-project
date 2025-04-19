FROM node:18-alpine

# Install build dependencies
RUN apk add --no-cache \
    python3 \
    make \
    g++ \
    curl

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the code
COPY . .

# Build the application
RUN npm run build

# Remove build dependencies to optimize image size
RUN apk del python3 make g++

# Create a non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nextjs -u 1001 && \
    chown -R nextjs:nodejs /app

USER nextjs

# Healthcheck
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:3000/api/health || exit 1

# Expose port 3000
EXPOSE 3000

# Start the application
CMD ["npm", "start"]
