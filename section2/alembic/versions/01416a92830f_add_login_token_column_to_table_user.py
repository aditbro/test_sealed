"""add login_token column to table user

Revision ID: 01416a92830f
Revises: cc71922459fe
Create Date: 2020-07-20 16:57:16.231698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01416a92830f'
down_revision = 'cc71922459fe'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'user',
        sa.Column('login_token', sa.String)
    )


def downgrade():
    op.drop_column(
        'user',
        'login_token'
    )
