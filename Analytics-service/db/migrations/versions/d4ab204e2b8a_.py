"""empty message

Revision ID: d4ab204e2b8a
Revises: 98a45e572254
Create Date: 2023-09-08 19:27:00.411882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4ab204e2b8a'
down_revision = '98a45e572254'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('location', schema=None) as batch_op:
        batch_op.alter_column('avg_living_cost',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               type_=sa.String(length=20),
               existing_nullable=True)
        batch_op.alter_column('population',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=20),
               existing_nullable=True)
        batch_op.alter_column('avg_income',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               type_=sa.String(length=20),
               existing_nullable=True)
        batch_op.alter_column('summer_comfort_index',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               type_=sa.String(length=20),
               existing_nullable=True)
        batch_op.alter_column('winter_comfort_index',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               type_=sa.String(length=20),
               existing_nullable=True)
        batch_op.alter_column('unemployment_rate',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               type_=sa.String(length=20),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('location', schema=None) as batch_op:
        batch_op.alter_column('unemployment_rate',
               existing_type=sa.String(length=20),
               type_=sa.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
        batch_op.alter_column('winter_comfort_index',
               existing_type=sa.String(length=20),
               type_=sa.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
        batch_op.alter_column('summer_comfort_index',
               existing_type=sa.String(length=20),
               type_=sa.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
        batch_op.alter_column('avg_income',
               existing_type=sa.String(length=20),
               type_=sa.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
        batch_op.alter_column('population',
               existing_type=sa.String(length=20),
               type_=sa.INTEGER(),
               existing_nullable=True)
        batch_op.alter_column('avg_living_cost',
               existing_type=sa.String(length=20),
               type_=sa.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)

    # ### end Alembic commands ###
