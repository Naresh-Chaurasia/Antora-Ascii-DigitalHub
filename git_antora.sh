
echo "Skip Building Antora site..."
sleep 1
# npm run build

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