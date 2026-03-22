-- database/schema.sql

PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;

-- ============================================================
-- SCHEMA VERSION TRACKING
-- ============================================================
CREATE TABLE IF NOT EXISTS schema_version (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    version     TEXT NOT NULL UNIQUE,
    description TEXT,
    applied_at  DATETIME DEFAULT (datetime('now')),
    is_deleted  BOOLEAN DEFAULT 0
);

INSERT OR IGNORE INTO schema_version (version, description)
VALUES ('1.0.0', 'Initial schema creation');

-- ============================================================
-- SITE CONFIGURATION
-- ============================================================
CREATE TABLE IF NOT EXISTS site_config (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    key                 TEXT NOT NULL UNIQUE,
    value               TEXT,
    description         TEXT,
    created_at          DATETIME DEFAULT (datetime('now')),
    updated_at          DATETIME DEFAULT (datetime('now')),
    is_visible          BOOLEAN DEFAULT 1,
    is_deleted          BOOLEAN DEFAULT 0
);

-- ============================================================
-- SOCIAL LINKS
-- ============================================================
CREATE TABLE IF NOT EXISTS social_links (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    platform    TEXT NOT NULL,
    url         TEXT NOT NULL,
    icon_class  TEXT,
    display_order INTEGER DEFAULT 0,
    created_at  DATETIME DEFAULT (datetime('now')),
    updated_at  DATETIME DEFAULT (datetime('now')),
    is_visible  BOOLEAN DEFAULT 1,
    is_deleted  BOOLEAN DEFAULT 0
);

-- ============================================================
-- DEVELOPER PROFILE
-- ============================================================
CREATE TABLE IF NOT EXISTS profile (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name       TEXT NOT NULL,
    title           TEXT NOT NULL,
    tagline         TEXT,
    bio_short       TEXT,
    bio_long        TEXT,
    avatar_url      TEXT,
    resume_url      TEXT,
    email           TEXT,
    phone           TEXT,
    location        TEXT,
    available_for_work BOOLEAN DEFAULT 1,
    created_at      DATETIME DEFAULT (datetime('now')),
    updated_at      DATETIME DEFAULT (datetime('now')),
    is_visible      BOOLEAN DEFAULT 1,
    is_deleted      BOOLEAN DEFAULT 0
);

-- ============================================================
-- EDUCATION
-- ============================================================
CREATE TABLE IF NOT EXISTS education (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    institution     TEXT NOT NULL,
    degree          TEXT NOT NULL,
    field_of_study  TEXT,
    start_date      TEXT,
    end_date        TEXT,
    gpa             TEXT,
    description     TEXT,
    logo_url        TEXT,
    location        TEXT,
    display_order   INTEGER DEFAULT 0,
    created_at      DATETIME DEFAULT (datetime('now')),
    updated_at      DATETIME DEFAULT (datetime('now')),
    is_visible      BOOLEAN DEFAULT 1,
    is_deleted      BOOLEAN DEFAULT 0
);

-- ============================================================
-- EXPERIENCE
-- ============================================================
CREATE TABLE IF NOT EXISTS experience (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    company         TEXT NOT NULL,
    position        TEXT NOT NULL,
    location        TEXT,
    employment_type TEXT DEFAULT 'Full-time',
    start_date      TEXT,
    end_date        TEXT,
    is_current      BOOLEAN DEFAULT 0,
    description     TEXT,
    logo_url        TEXT,
    company_url     TEXT,
    display_order   INTEGER DEFAULT 0,
    created_at      DATETIME DEFAULT (datetime('now')),
    updated_at      DATETIME DEFAULT (datetime('now')),
    is_visible      BOOLEAN DEFAULT 1,
    is_deleted      BOOLEAN DEFAULT 0
);

CREATE TABLE IF NOT EXISTS experience_achievements (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    experience_id   INTEGER NOT NULL REFERENCES experience(id),
    achievement     TEXT NOT NULL,
    display_order   INTEGER DEFAULT 0,
    created_at      DATETIME DEFAULT (datetime('now')),
    updated_at      DATETIME DEFAULT (datetime('now')),
    is_visible      BOOLEAN DEFAULT 1,
    is_deleted      BOOLEAN DEFAULT 0
);

-- ============================================================
-- SKILLS
-- ============================================================
CREATE TABLE IF NOT EXISTS skill_categories (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    name            TEXT NOT NULL UNIQUE,
    icon_class      TEXT,
    display_order   INTEGER DEFAULT 0,
    created_at      DATETIME DEFAULT (datetime('now')),
    updated_at      DATETIME DEFAULT (datetime('now')),
    is_visible      BOOLEAN DEFAULT 1,
    is_deleted      BOOLEAN DEFAULT 0
);

CREATE TABLE IF NOT EXISTS skills (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id     INTEGER NOT NULL REFERENCES skill_categories(id),
    name            TEXT NOT NULL,
    proficiency     INTEGER DEFAULT 80 CHECK(proficiency BETWEEN 0 AND 100),
    icon_url        TEXT,
    display_order   INTEGER DEFAULT 0,
    created_at      DATETIME DEFAULT (datetime('now')),
    updated_at      DATETIME DEFAULT (datetime('now')),
    is_visible      BOOLEAN DEFAULT 1,
    is_deleted      BOOLEAN DEFAULT 0
);

-- ============================================================
-- TAGS (Reusable)
-- ============================================================
CREATE TABLE IF NOT EXISTS tags (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    tag_id      INTEGER NOT NULL UNIQUE,
    name        TEXT NOT NULL UNIQUE,
    slug        TEXT NOT NULL UNIQUE,
    display_order INTEGER NOT NULL,
    created_at  DATETIME DEFAULT (datetime('now')),
    updated_at  DATETIME DEFAULT (datetime('now')),
    is_visible  BOOLEAN DEFAULT 1,
    is_deleted  BOOLEAN DEFAULT 0
);

-- ============================================================
-- PROJECTS
-- ============================================================
CREATE TABLE IF NOT EXISTS projects (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    title           TEXT NOT NULL,
    slug            TEXT NOT NULL UNIQUE,
    short_desc      TEXT,
    long_desc       TEXT,
    image_url       TEXT,
    demo_url        TEXT,
    github_url      TEXT,
    workflow_url    TEXT,                          -- n8n.io/creators or workflow publications
    dashboard_url   TEXT,                          -- Published dashboards
    integration_url TEXT,                          -- External app/platform integrations
    status          TEXT DEFAULT 'completed',
    featured        BOOLEAN DEFAULT 0,
    display_order   INTEGER DEFAULT 0,
    publish_date    DATE,
    created_at      DATETIME DEFAULT (datetime('now')),
    updated_at      DATETIME DEFAULT (datetime('now')),
    is_visible      BOOLEAN DEFAULT 1,
    is_deleted      BOOLEAN DEFAULT 0
);

CREATE TABLE IF NOT EXISTS project_tags (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id  INTEGER NOT NULL REFERENCES projects(id),
    tag_id      INTEGER NOT NULL REFERENCES tags(id),
    created_at  DATETIME DEFAULT (datetime('now')),
    updated_at  DATETIME DEFAULT (datetime('now')),
    is_visible  BOOLEAN DEFAULT 1,
    is_deleted  BOOLEAN DEFAULT 0,
    UNIQUE(project_id, tag_id)
);

-- ============================================================
-- CERTIFICATIONS
-- ============================================================
CREATE TABLE IF NOT EXISTS certifications (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    title           TEXT NOT NULL,
    issuer          TEXT NOT NULL,
    issue_date      TEXT,
    expiry_date     TEXT,
    credential_id   TEXT,
    credential_url  TEXT,
    logo_url        TEXT,
    course_link     TEXT,
    estimated_effort TEXT,
    description     TEXT,
    featured        BOOLEAN DEFAULT 0,
    display_order   INTEGER DEFAULT 0,
    created_at      DATETIME DEFAULT (datetime('now')),
    updated_at      DATETIME DEFAULT (datetime('now')),
    is_visible      BOOLEAN DEFAULT 1,
    is_deleted      BOOLEAN DEFAULT 0
);

-- ============================================================
-- BLOG POSTS
-- ============================================================
CREATE TABLE IF NOT EXISTS blog_posts (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    title           TEXT NOT NULL,
    slug            TEXT NOT NULL UNIQUE,
    excerpt         TEXT,
    content         TEXT,
    cover_image_url TEXT,
    post_url        TEXT,                          
    read_time       INTEGER DEFAULT 5,
    featured        BOOLEAN DEFAULT 0,
    publish_date    DATE,
    display_order   INTEGER DEFAULT 0,
    created_at      DATETIME DEFAULT (datetime('now')),
    updated_at      DATETIME DEFAULT (datetime('now')),
    is_visible      BOOLEAN DEFAULT 1,
    is_deleted      BOOLEAN DEFAULT 0
);

CREATE TABLE IF NOT EXISTS blog_post_tags (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id     INTEGER NOT NULL REFERENCES blog_posts(id),
    tag_id      INTEGER NOT NULL REFERENCES tags(id),
    created_at  DATETIME DEFAULT (datetime('now')),
    updated_at  DATETIME DEFAULT (datetime('now')),
    is_visible  BOOLEAN DEFAULT 1,
    is_deleted  BOOLEAN DEFAULT 0,
    UNIQUE(post_id, tag_id)
);

-- ============================================================
-- TESTIMONIALS
-- ============================================================
CREATE TABLE IF NOT EXISTS testimonials (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    author_name     TEXT NOT NULL,
    author_title    TEXT,
    author_company  TEXT,
    author_avatar   TEXT,
    content         TEXT NOT NULL,
    rating          INTEGER DEFAULT 5 CHECK(rating BETWEEN 1 AND 5),
    relationship    TEXT,
    featured        BOOLEAN DEFAULT 0,
    display_order   INTEGER DEFAULT 0,
    created_at      DATETIME DEFAULT (datetime('now')),
    updated_at      DATETIME DEFAULT (datetime('now')),
    is_visible      BOOLEAN DEFAULT 1,
    is_deleted      BOOLEAN DEFAULT 0
);

-- ============================================================
-- ANALYTICS CONFIG
-- ============================================================
CREATE TABLE IF NOT EXISTS analytics_config (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    analytics_enabled   BOOLEAN DEFAULT 0,
    provider            TEXT,
    tracking_id         TEXT,
    created_at          DATETIME DEFAULT (datetime('now')),
    updated_at          DATETIME DEFAULT (datetime('now')),
    is_visible          BOOLEAN DEFAULT 1,
    is_deleted          BOOLEAN DEFAULT 0
);

-- ============================================================
-- INDEXES
-- ============================================================
CREATE INDEX IF NOT EXISTS idx_projects_featured     ON projects(featured)     WHERE is_deleted = 0;
CREATE INDEX IF NOT EXISTS idx_projects_visible      ON projects(is_visible)   WHERE is_deleted = 0;
CREATE INDEX IF NOT EXISTS idx_projects_publish_date ON projects(publish_date) WHERE is_deleted = 0;
CREATE INDEX IF NOT EXISTS idx_blog_featured         ON blog_posts(featured)   WHERE is_deleted = 0;
CREATE INDEX IF NOT EXISTS idx_blog_visible          ON blog_posts(is_visible) WHERE is_deleted = 0;
CREATE INDEX IF NOT EXISTS idx_blog_publish_date     ON blog_posts(publish_date) WHERE is_deleted = 0;
CREATE INDEX IF NOT EXISTS idx_skills_category       ON skills(category_id)    WHERE is_deleted = 0;
CREATE INDEX IF NOT EXISTS idx_experience_order      ON experience(display_order) WHERE is_deleted = 0;