 SELECT c.company_code, c.founder,
 (
     SELECT COUNT(DISTINCT lead_manager_code)
     FROM Lead_Manager
     WHERE Lead_Manager.company_code = c.company_code
 ) AS Lead_Manager_Count,
(
    SELECT COUNT(DISTINCT senior_manager_code)
    FROM Senior_Manager
    WHERE Senior_Manager.company_code = c.company_code
) AS Senior_Manager_Count,
(
    SELECT COUNT(DISTINCT manager_code)
    FROM Manager
    WHERE Manager.company_code = c.company_code
) AS Manager_Count,
(
    SELECT COUNT(DISTINCT employee_code)
    FROM Employee
    WHERE Employee.company_code = c.company_code
)  AS Employee_Count
FROM Company AS c
ORDER BY c.company_code;