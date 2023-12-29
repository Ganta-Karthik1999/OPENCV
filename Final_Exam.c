#include "freertos/task.h"
#include "freertos/semphr.h"

#include <stdlib.h>
#include <string.h>

void vTask1(void *param)
{
while (1)
{
 printf("I am LOW Priority Task\n");
 vTaskDelay(1000 / portTICK_PERIOD_MS);
}
}

void vTask2(void *param)
{
while (1)
{
printf("I am MEDIUM Priority Task\n");
vTaskDelay(1000 / portTICK_PERIOD_MS);
}
}

void vTask3(void *param)
{
while (1)
{
printf("I am HIGH Priority Task\n");
vTaskDelay(1000 / portTICK_PERIOD_MS);
}
}

void app_main()
{

TaskHandle_t handle1 = NULL;
TaskHandle_t handle2 = NULL;
TaskHandle_t handle3 = NULL;

xTaskCreate(vTask1, "Task1", 0x1000, (void *)NULL, 1, &handle1);
xTaskCreate(vTask2, "Task2", 0x1000, (void *)NULL, 2, &handle2);
xTaskCreate(vTask3, "Task3", 0x1000, (void *)NULL, 10, &handle3);

while (1)
 {
printf("Main Thread Task\n");
 vTaskDelay(1000 / portTICK_PERIOD_MS);
 }
}