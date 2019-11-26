BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "tracker_record" (
	"recordID"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"type"	varchar(2) NOT NULL,
	"status"	varchar(2) NOT NULL,
	"title"	varchar(32),
	"description"	varchar(256),
	"dateCreated"	datetime NOT NULL,
	"dateModified"	datetime NOT NULL,
	"assigned_id"	integer NOT NULL,
	"comments_id"	integer NOT NULL,
	"originator_id"	integer NOT NULL,
	"projectId_id"	integer NOT NULL,
	FOREIGN KEY("assigned_id") REFERENCES "tracker_account"("accountID") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("projectId_id") REFERENCES "tracker_project"("projectID") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("originator_id") REFERENCES "tracker_account"("accountID") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("comments_id") REFERENCES "tracker_recordcomment"("commentID") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "tracker_recordcomment" (
	"commentID"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"title"	varchar(32),
	"content"	varchar(256),
	"dateCreated"	datetime NOT NULL,
	"dateModified"	datetime NOT NULL,
	"owner_id"	integer NOT NULL,
	FOREIGN KEY("owner_id") REFERENCES "tracker_account"("accountID") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "tracker_project" (
	"projectID"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	varchar(64) NOT NULL,
	"description"	varchar(256),
	"dateCreated"	datetime NOT NULL,
	"dateModified"	datetime NOT NULL,
	"owner_id"	integer NOT NULL,
	FOREIGN KEY("owner_id") REFERENCES "tracker_account"("accountID") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "tracker_account" (
	"accountID"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	varchar(32),
	"description"	varchar(256),
	"email"	varchar(254) NOT NULL,
	"dateCreated"	datetime NOT NULL,
	"dateModified"	datetime NOT NULL,
	"priority"	varchar(2) NOT NULL
);
INSERT INTO "tracker_record" ("recordID","type","status","title","description","dateCreated","dateModified","assigned_id","comments_id","originator_id","projectId_id") VALUES (1,'WK','IN','First record','blah','2019-11-26 17:52:18.394003','2019-11-26 17:52:18.394003',1,1,1,1);
INSERT INTO "tracker_recordcomment" ("commentID","title","content","dateCreated","dateModified","owner_id") VALUES (1,'Adding first comment','Here it is','2019-11-26 17:52:15.658943','2019-11-26 17:52:15.659934',1);
INSERT INTO "tracker_project" ("projectID","name","description","dateCreated","dateModified","owner_id") VALUES (1,'Proj1','First project','2019-11-26 17:50:51.353859','2019-11-26 17:50:51.353859',1);
INSERT INTO "tracker_account" ("accountID","name","description","email","dateCreated","dateModified","priority") VALUES (1,'Paul','Admin','pchalmers2011@gmail.com','','','');
CREATE INDEX IF NOT EXISTS "tracker_record_projectId_id_932c4f00" ON "tracker_record" (
	"projectId_id"
);
CREATE INDEX IF NOT EXISTS "tracker_record_originator_id_fc9ee034" ON "tracker_record" (
	"originator_id"
);
CREATE INDEX IF NOT EXISTS "tracker_record_comments_id_f26b84bc" ON "tracker_record" (
	"comments_id"
);
CREATE INDEX IF NOT EXISTS "tracker_record_assigned_id_31f838c2" ON "tracker_record" (
	"assigned_id"
);
CREATE INDEX IF NOT EXISTS "tracker_recordcomment_owner_id_b7ef925b" ON "tracker_recordcomment" (
	"owner_id"
);
CREATE INDEX IF NOT EXISTS "tracker_project_owner_id_967dedbe" ON "tracker_project" (
	"owner_id"
);
COMMIT;
