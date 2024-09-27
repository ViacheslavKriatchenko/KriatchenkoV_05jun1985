SELECT distinct p.product_name from public.products p;

SELECT 
	p.product_id, p.product_name, p.price 
FROM 
	public.products p
JOIN 
	public.nutritional_information as ni using(product_id)
WHERE
	ni.fiber > 5;
	
SELECT 
	p.product_name 
FROM 
	public.products p
JOIN 
	public.nutritional_information as ni using(product_id)
ORDER BY ni.protein desc
LIMIT 1;

SELECT 
    p.category_id,
    SUM(p.calories) AS sum_calories
FROM 
    Products p
JOIN 
    Nutritional_Information as ni using(product_id)
WHERE 
    ni.fat > 0
GROUP BY 
    p.category_id;
	
SELECT c.category_name, round(avg(p.price), 2) as средняя_цена
FROM public.categories c
JOIN public.products as p using(category_id)
GROUP BY c.category_name