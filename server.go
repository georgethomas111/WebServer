package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

//Displays a paticular file in a folder
func DispFile(w http.ResponseWriter, r *http.Request) {
	data, err := ioutil.ReadFile(r.URL.Path[1:])
	if err == nil {
		fmt.Fprintf(w, "%s", data)
	} else {
		fmt.Fprintf(w, "%s", err.Error())
	}
}

// Lists the Files in the current folder.
func ListFiles(w http.ResponseWriter, r *http.Request) {
	files, err := ioutil.ReadDir(".")
	if err == nil {
		for _, file := range files {
			fmt.Fprintf(w, "<a href='%s'>%s</a><br/>", file.Name(), file.Name())
		}
	} else {
		fmt.Fprintf(w, "%s", err.Error())
	}
}

func main() {
	http.HandleFunc("/list", ListFiles)
	http.HandleFunc("/", DispFile)
	http.ListenAndServe(":8080", nil)
}
