SELECT max(sum(transaction.qty_transaction)) as quantity, product.name_product as product, customer.gender_customer FROM customer, transaction, product WHERE product.id_product=transaction.id_product GROUP BY customer.gender

SELECT customer.name_customer, max(sum(transaction.total_price_transaction)) FROM customer, transaction WHERE transaction.id_transaction=customer.id_customer LIMIT 1

SELECT HOUR(time_transaction), COUNT(id_transaction FROM transaction GROUP BY HOUR(time_transaction) DIV 2 GROUP BY HOUR(time_transaction)