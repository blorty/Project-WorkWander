"""empty message

Revision ID: 2f5b5f0e3863
Revises: 
Create Date: 2023-06-12 08:50:50.028425

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f5b5f0e3863'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('company_reviews')
    op.drop_table('salaries')
    op.drop_table('applications')
    op.drop_table('appliedjobs')
    op.drop_table('user')
    op.drop_table('applied_jobs')
    op.drop_table('companyreviews')
    op.drop_table('savedjobs')
    with op.batch_alter_table('companies', schema=None) as batch_op:
        batch_op.drop_constraint('fk_companies_company_id_companies', type_='foreignkey')
        batch_op.drop_column('location')
        batch_op.drop_column('description')
        batch_op.drop_column('company_id')

    with op.batch_alter_table('jobs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint('fk_jobs_company_review_id_company_reviews', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_jobs_user_id_users'), 'users', ['user_id'], ['id'])
        batch_op.drop_column('company_review_id')
        batch_op.drop_column('User_id')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_users_email'), ['email'])
        batch_op.create_unique_constraint(batch_op.f('uq_users_username'), ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_users_username'), type_='unique')
        batch_op.drop_constraint(batch_op.f('uq_users_email'), type_='unique')

    with op.batch_alter_table('jobs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('User_id', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('company_review_id', sa.INTEGER(), nullable=True))
        batch_op.drop_constraint(batch_op.f('fk_jobs_user_id_users'), type_='foreignkey')
        batch_op.create_foreign_key('fk_jobs_company_review_id_company_reviews', 'company_reviews', ['company_review_id'], ['id'])
        batch_op.create_foreign_key(None, 'users', ['User_id'], ['id'])
        batch_op.drop_column('user_id')

    with op.batch_alter_table('companies', schema=None) as batch_op:
        batch_op.add_column(sa.Column('company_id', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('description', sa.VARCHAR(), nullable=False))
        batch_op.add_column(sa.Column('location', sa.VARCHAR(), nullable=False))
        batch_op.create_foreign_key('fk_companies_company_id_companies', 'companies', ['company_id'], ['id'])

    op.create_table('savedjobs',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('job_id', sa.VARCHAR(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('company', sa.VARCHAR(), nullable=True),
    sa.Column('title', sa.VARCHAR(), nullable=True),
    sa.Column('location', sa.VARCHAR(), nullable=True),
    sa.Column('description', sa.VARCHAR(), nullable=True),
    sa.Column('salary', sa.VARCHAR(), nullable=True),
    sa.Column('link', sa.VARCHAR(), nullable=True),
    sa.Column('date', sa.VARCHAR(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_savedjobs_user_id_user'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('companyreviews',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('job_id', sa.VARCHAR(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('review', sa.VARCHAR(), nullable=False),
    sa.Column('rating', sa.VARCHAR(), nullable=False),
    sa.Column('company', sa.VARCHAR(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_companyreviews_user_id_user'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('applied_jobs',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('job_id', sa.INTEGER(), nullable=False),
    sa.Column('applied_date', sa.DATE(), nullable=False),
    sa.Column('salary', sa.INTEGER(), nullable=False),
    sa.Column('company_review', sa.VARCHAR(), nullable=False),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.id'], name='fk_applied_jobs_job_id_jobs'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_applied_jobs_user_id_users'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), nullable=False),
    sa.Column('password', sa.VARCHAR(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('appliedjobs',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('job_id', sa.VARCHAR(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('company', sa.VARCHAR(), nullable=True),
    sa.Column('title', sa.VARCHAR(), nullable=True),
    sa.Column('location', sa.VARCHAR(), nullable=True),
    sa.Column('description', sa.VARCHAR(), nullable=True),
    sa.Column('salary', sa.VARCHAR(), nullable=True),
    sa.Column('link', sa.VARCHAR(), nullable=True),
    sa.Column('date', sa.VARCHAR(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_appliedjobs_user_id_user'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('applications',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('job_id', sa.INTEGER(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.id'], name='fk_applications_job_id_jobs'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_applications_user_id_users'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('salaries',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('salary', sa.VARCHAR(), nullable=False),
    sa.Column('job_id', sa.INTEGER(), nullable=True),
    sa.Column('User_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['User_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.id'], name='fk_salaries_job_id_jobs'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('company_reviews',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('review', sa.VARCHAR(), nullable=False),
    sa.Column('company_id', sa.INTEGER(), nullable=True),
    sa.Column('User_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['User_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], name='fk_company_reviews_company_id_companies'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
