CREATE TABLE IF NOT EXISTS posts(
  id TEXT PRIMARY KEY,
  cuando INTEGER NOT NULL,          -- fecha de publicación en milisegundos
  tipo TEXT NOT NULL,               -- reel | image | story | carousel
  caption TEXT,
  media TEXT NOT NULL,              -- lista JSON de archivos
  redes TEXT NOT NULL,              -- lista JSON: ig, fb, tiktok
  estado TEXT NOT NULL DEFAULT 'programado',
  detalle TEXT NOT NULL DEFAULT '{}',
  creado INTEGER NOT NULL
);
CREATE INDEX IF NOT EXISTS posts_pendientes ON posts(estado, cuando);
CREATE TABLE IF NOT EXISTS ajustes(clave TEXT PRIMARY KEY, valor TEXT NOT NULL);
