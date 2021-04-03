FILES="./submissions/*"
mkdir -p "./unzipped_submissions"
mkdir -p "./strong_submissions"
for f in $FILES
do
    echo "${f}"
    basename="$(basename ${f})"
    echo "${basename}"
    dirname="$(dirname  ${f})"
    
    if [[ "${basename}" != "" ]]; then
    	mkdir -p "./unzipped_submissions/${basename}"
        unzip "${f}" -d "./unzipped_submissions/${basename}"
    fi
    
done
