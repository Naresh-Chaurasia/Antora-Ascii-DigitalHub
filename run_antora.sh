echo "Building the site using npm..."
npm run build
sleep 1

# Check if build failed
if [ $? -ne 0 ]; then
  echo "Build failed. Terminating process."
  exit 1
fi

echo "Build completed."
sleep 1

echo "Starting deployment process..."
sleep 1

echo "Adding all files to git staging..."
sleep 1
git add .

echo "Capturing current timestamp..."
sleep 1
my_date=$(date)
echo "Timestamp: $my_date"

sleep 1
echo "Creating git commit with timestamp..."
git commit -m "Macbook Pro, Checkin Timestamp::$my_date"

sleep 1
echo "Pushing changes to origin main..."
git push origin main

sleep 1
echo "https://naresh-chaurasia.github.io/Antora-Ascii-DigitalHub/my-component/1/index.html"

sleep 1
echo "Starting local server at http://localhost:8080 ..."
python3 -m http.server 8080 --directory build/site