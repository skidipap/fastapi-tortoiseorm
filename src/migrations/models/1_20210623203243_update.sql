-- upgrade --
ALTER TABLE "event" RENAME TO "users";
-- downgrade --
ALTER TABLE "users" RENAME TO "event";
