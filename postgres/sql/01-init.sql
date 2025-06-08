CREATE TABLE data_sensors (
  id NUMERIC,
  date TIMESTAMP,
  value NUMERIC,
  unit VARCHAR(10)
);

CREATE TABLE metadata_sensors (
  id NUMERIC,
  model VARCHAR(50),
  serial_number VARCHAR(50),
  tag VARCHAR(50),
  type VARCHAR(50)
);
  
INSERT INTO metadata_sensors (id, model, serial_number, tag, type) VALUES
(1, 'DHT11', 'SN-DHT11-001', 'sensor_temp_hum_01', 'temperatura/umidade'),
(2, 'DHT11', 'SN-DHT11-002', 'sensor_temp_hum_02', 'temperatura/umidade'),
(3, 'DHT11', 'SN-DHT11-003', 'sensor_temp_hum_03', 'temperatura/umidade'),
(4, 'DHT11', 'SN-DHT11-004', 'sensor_temp_hum_04', 'temperatura/umidade');
