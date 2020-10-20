# FROM rabbitmq:3.8.9
FROM rabbitmq:3.8.9

RUN rabbitmq-plugins enable --offline rabbitmq_management && rabbitmq-plugins enable --offline rabbitmq_mqtt

EXPOSE 15672
EXPOSE 8883
