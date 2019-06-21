docker:
	docker run \
		--tty \
		--interactive \
		--rm --volume "$(PWD)":/home/docker \
		--workdir /home/docker \
		--user docker \
		r-base \
		/usr/bin/Rscript hello.r
flask:
	/usr/bin/env python hello.py

version:
	docker run --tty --interactive --rm r-base /usr/bin/Rscript --version
