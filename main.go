package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"net/http"
	"net/url"

	log "github.com/Sirupsen/logrus"
)

const (
	// Graph api endpoint for node operations
	graphEndpoint = "https://graph.facebook.com/v2.7/%s"
)

var (
	token = flag.String("token", "", "Facebook access token")
)

func main() {
	log.Info("starting facebook eraser")
	flag.Parse()

	if *token == "" {
		log.Fatal("must specify token flag")
	}

	var u, err = url.Parse(fmt.Sprintf(graphEndpoint, "me"))
	if err != nil {
		log.WithField("err", err).Fatal("parsing url")
	}
	var query = u.Query()
	query.Add("access_token", *token)
	query.Add("fields", "posts.limit(10)")
	u.RawQuery = query.Encode()

	var resp *http.Response
	resp, err = http.Get(u.String())
	if err != nil {
		log.WithField("err", err).Fatal("getting posts listing")
	}

	var posts []byte
	posts, err = ioutil.ReadAll(resp.Body)
	if err != nil {
		log.WithField("err", err).Fatal("decoding posts listing")
	}

	log.WithField("posts", string(posts)).Info("last 10 posts")
}
