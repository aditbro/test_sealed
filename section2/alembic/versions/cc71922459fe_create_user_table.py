"""create user table

Revision ID: cc71922459fe
Revises:
Create Date: 2020-07-17 17:43:13.715089

"""
from alembic import op
from sqlalchemy.sql import func
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc71922459fe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('username', sa.String, unique=True, index=True),
        sa.Column('email', sa.String, unique=True, index=True),
        sa.Column('name', sa.String),
        sa.Column('is_email_verified', sa.Boolean),
        sa.Column('created', sa.DateTime(timezone=True), server_default=func.now()),
        sa.Column('updated', sa.DateTime(timezone=True), onupdate=func.now()),
        sa.Column('telephone', sa.String),
        sa.Column('password', sa.String)
    )


def downgrade():
    op.drop_table('user')
