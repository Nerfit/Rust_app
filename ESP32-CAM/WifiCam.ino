#include <WebServer.h>
#include <WiFi.h>
#include <esp32cam.h>
#include "esp_camera.h"


const char* WIFI_SSID = "Net_227";
const char* WIFI_PASS = "******";

WebServer server(80);

static auto hiRes = esp32cam::Resolution::find(1600, 1200);



void
serveJpg()
{
  auto frame = esp32cam::capture();
  if (frame == nullptr) {
    Serial.println("CAPTURE FAIL");
    server.send(503, "", "");
    return;
  }
  Serial.printf("CAPTURE OK %dx%d %db\n", frame->getWidth(), frame->getHeight(),
                static_cast<int>(frame->size()));

  server.setContentLength(frame->size());
  server.send(200, "image/jpeg");
  WiFiClient client = server.client();
  frame->writeTo(client);
}

void
handleJpgHi()
{
  if (!esp32cam::Camera.changeResolution(hiRes)) {
    Serial.println("SET-HI-RES FAIL");
  }
  serveJpg();
}

void
handleJpg()
{
  server.sendHeader("Location", "/cam-hi.jpg");
  server.send(302, "", "");
}


void
setup()
{
  Serial.begin(115200);
  Serial.println();
  //pinMode(4, OUTPUT);  Flash Led Pin

  {
    using namespace esp32cam;
    Config cfg;
    cfg.setPins(pins::AiThinker);
    cfg.setResolution(hiRes);
    cfg.setBufferCount(2);
    cfg.setJpeg(90);


    bool ok = Camera.begin(cfg);
    Serial.println(ok ? "CAMERA OK" : "CAMERA FAIL");
  }

  WiFi.persistent(false);
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }

  Serial.print("http://");
  Serial.println(WiFi.localIP());
  Serial.println("  /cam-hi.jpg");
  server.on("/cam-hi.jpg", handleJpgHi);

  server.begin();
}

void
loop()
{
  server.handleClient();
}
