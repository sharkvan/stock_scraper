#! /bin/bash
docker run \
        --rm \
        -v `pwd`:/stock-scraper \
        -w /stock-scraper \
        scrapy \
        crawl profile \
        -a folder=/stock-scraper \
        -a symbol='/stock-scraper'
