-- Stakeholder summary metrics for D06
SELECT
  COUNT(*) AS total_records,
  AVG(CAST(overallocated AS FLOAT)) AS overallocated_rate
FROM resource_utilization;

SELECT *
FROM resource_utilization
ORDER BY 1
LIMIT 10;
