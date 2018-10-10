echo Downloading pronto data

mkdir pronto
cd pronto

curl -o pronto.csv https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv?accessType=DOWNLOAD
head pronto.csv

echo All done
