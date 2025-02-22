const express = require('express');
const app = express();
const products = [{ id: 1, name: "Laptop", price: 999 }];

app.use(express.json()); // Middleware to parse JSON request bodies

// Endpoint to fetch all products
app.get('/api/catalog/products', (req, res) => res.json(products));

// Endpoint to add a new product
app.post('/api/catalog/products', (req, res) => {
    const { name, price } = req.body;
    
    // Input validation to prevent malformed data
    if (!name || price <= 0) return res.status(400).json({ error: "Invalid input" });

    const product = { id: products.length + 1, name, price };
    products.push(product);
    res.status(201).json(product);
});

app.listen(5002, () => console.log('Catalog Service running on port 5002'));
