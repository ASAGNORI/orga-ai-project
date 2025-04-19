FROM node:18-alpine

# Instalar Python, make e g++ (necessários para node-gyp)
RUN apk add --no-cache python3 make g++

WORKDIR /app

# Copiar package.json e package-lock.json primeiro para aproveitar o cache do Docker
COPY package*.json ./

# Instalar as dependências do projeto
RUN npm install

# Copiar o restante do código
COPY . .

# Rodar o build da aplicação
RUN npm run build

# Remover dependências de build (otimização para diminuir o tamanho da imagem)
RUN apk del python3 make g++

# Expor a porta
EXPOSE 3000

# Comando para rodar a aplicação em modo de desenvolvimento
CMD ["npm", "run", "dev"]
