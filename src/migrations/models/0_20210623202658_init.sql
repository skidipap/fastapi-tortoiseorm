-- upgrade --
CREATE TABLE IF NOT EXISTS "event" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS "items" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "item" VARCHAR(255) NOT NULL,
    "owner_id" INT NOT NULL REFERENCES "event" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSON NOT NULL
);
