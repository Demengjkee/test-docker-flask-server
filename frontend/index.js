#!/usr/bin/env node

'use strict';

var http = require('http');
var url = require('url');
var fs = require('fs')

/* I'm doing promises wrong :)  
function getPage() {
    return new Promise(function(resolve, reject) {
        fs.readFile(__dirname + '/index.html', function(err, data) {
            err ? reject(err) : resolve(data);
        });
    });
    
}
*/

function getPage() {
    var page = fs.readFileSync('index.html', 'utf8');
    return page;
}

function serveGet(req, resp, path) {
    var page;
    var statusCode;
    if(path == '/') {
        page = getPage();
        statusCode = 200;
    } else {
        page = "<h1> Not Found </h1>";
        statusCode = 404;
    }
    console.log("[INFO] " + path + " - GET - " + statusCode);
    resp.writeHead(statusCode, {"Content-Type": "text/html"});
    resp.write(page);
    resp.end();
}

function servePost(req, resp, path) {
    var backendUrl = process.env.BACKEND_URL || 'defult.backend.local';
    console.log("POST");
    resp.writeHead(200);
    resp.end("ULALALA");
}

var server = http.createServer(function(req, resp) {
    var path = url.parse(req.url).pathname;
    var method = req.method;
    if (method == 'GET') {
        serveGet(req, resp, path);
    } else if (method == 'POST') {
        servePost(req, resp, path);
    }
});

server.listen(8000);
