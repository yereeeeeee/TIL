-- a
SELECT 
  BillingCountry,
  SUM(Total) AS TotalSales
FROM invoices
GROUP BY BillingCountry;

-- b
SELECT 
  STRFTIME('%Y', InvoiceDate) AS Year,
  SUM(Total) AS TotalSales
FROM invoices
GROUP BY 
  STRFTIME('%Y', InvoiceDate);

-- c
SELECT
  BillingState,
  SUM(Total) AS TotalSales
FROM invoices
WHERE
  BillingCountry = 'USA' AND InvoiceDate > '2010-01-01'
GROUP BY BillingState;

-- d 
SELECT
  BillingCountry,
  Total AS MaxOrderAmount
FROM invoices
WHERE
  BillingCountry = 'Germany' OR BillingCountry = 'France'
GROUP BY BillingCountry
HAVING MAX(Total);