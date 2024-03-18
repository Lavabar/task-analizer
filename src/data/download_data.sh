curl https://zenodo.org/api/records/7182101/files-archive -o data/initial_data/ThePublicJiraDataset.zip
unzip data/initial_data/ThePublicJiraDataset.zip -d data/initial_data/tmp
mv data/initial_data/tmp/3.\ DataDump/mongodump-JiraRepos.archive data/initial_data
rm -rf data/initial_data/tmp
#install mongodb on your machine
mongorestore --gzip --archive=data/initial_data/3.\ DataDump/mongodump-JiraRepos.archive --nsFrom "JiraRepos.*" --nsTo "JiraRepos.*"