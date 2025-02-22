// server.js

const express = require('express');  // Import Express framework
const client = require('prom-client');  // Import Prometheus client library

const app = express();
const collectDefaultMetrics = client.collectDefaultMetrics;
collectDefaultMetrics();  // Enable default system metrics (CPU, Memory, etc.)

// Define a counter metric for tracking API requests
const requestCounter = new client.Counter({
  name: 'http_requests_total',
  help: 'Total number of HTTP requests received',
});

app.get('/', (req, res) => {
  requestCounter.inc();  // Increment counter on every request
  res.send('Hello, World!');
});

// Expose metrics endpoint for Prometheus to scrape
app.get('/metrics', async (req, res) => {
  res.set('Content-Type', client.register.contentType);
  res.end(await client.register.metrics());
});

// Start the Express server on port 3000
app.listen(3000, () => console.log('Server running on port 3000'));
