CREATE TABLE Customer_Table {
  id integer [primary key]
  customer_name string
}

CREATE TABLE costs {
  InstanceType varchar2(30)
  period date
  Total_costs double
}

CREATE TABLE FX_Table {
  Date date
  Rate double
}

CREATE TABLE Country_Table {
  id integer [primary key]
  city varchar2(30)
  country varchar2(30)
  sales_channel varchar2(5)
}

CREATE TABLE Sales_Data {
  category string
  subcategory string
  product_family varchar2(30)
  key_product varchar2(50)
  sku varchar2(100)
  description varchar2(150)
  grade varchar2(1)
  country_id integer
  cost_currency string
  cost_per_device integer
  sales_date date
  sold_currency string
  price_sold_per_device integer
  status string
  customer_id integer
  quantity integer
  sales_order_id integer
  serial integer
  bin_id varchar2(10)
}

Ref: Customer_Table.id > Sales_Data.customer_id
Ref: Country_Table.id > Sales_Data.country_id