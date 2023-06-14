"""empty message

Revision ID: 0a48baee3899
Revises: 2f5b5f0e3863
Create Date: 2023-06-14 15:08:00.896250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a48baee3899'
down_revision = '2f5b5f0e3863'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.Column('favorite', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.id'], name=op.f('fk_favorites_job_id_jobs')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_favorites_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_favorites'))
    )
    with op.batch_alter_table('jobs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('favorite', sa.Boolean(), nullable=False, server_default='False'))

    # Set existing rows in 'jobs' table to have 'favorite' value as False
    op.execute("UPDATE jobs SET favorite = 'False'")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('jobs', schema=None) as batch_op:
        batch_op.drop_column('favorite')

    op.drop_table('favorites')
    # ### end Alembic commands ###
