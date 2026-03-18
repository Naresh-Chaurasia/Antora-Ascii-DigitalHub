echo "Building the site using npm..."
npm run build
sleep 1

echo "Build completed."

echo "Starting local server at http://localhost:8080 ..."
python3 -m http.server 8080 --directory build/site