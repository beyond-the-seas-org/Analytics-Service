"""empty message

Revision ID: c821f6b27cb6
Revises: a5ac6834f794
Create Date: 2023-08-25 12:46:19.563942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c821f6b27cb6'
down_revision = 'a5ac6834f794'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('location', schema=None) as batch_op:
        batch_op.add_column(sa.Column('state_name', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('location', schema=None) as batch_op:
        batch_op.drop_column('state_name')

    # ### end Alembic commands ###
