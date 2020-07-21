"""create employee table

Revision ID: 67ba8d6496c9
Revises:
Create Date: 2020-07-21 21:23:48.091005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67ba8d6496c9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'employee',
        sa.Column('id', sa.String, primary_key=True),
        sa.Column('login', sa.String, unique=True),
        sa.Column('name', sa.String)
    )


def downgrade():
    op.drop_table('employee')
