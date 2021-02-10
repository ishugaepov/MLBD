docker run \
        --rm \
	--hostname=quickstart.cloudera \
	--privileged=true \
	-t -i \
	--publish-all=true \
	-p 8888:8888 \
	-p 9999:9999 \
	-p 8088:8088 \
	-p 7180:7180 \
	-p 80:80 \
	-v $(pwd)/..:/workspace \
	ishugaepov/mlbd \
	/usr/bin/docker-quickstart
