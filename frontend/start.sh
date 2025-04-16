#Iniciar o frontend
echo ""
echo "🖥️ Iniciando o frontend com npm..."
cd ../frontend || { echo "❌ Pasta 'frontend' não encontrada!"; exit 1; }
npm run dev