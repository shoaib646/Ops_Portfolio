#
#          docker pull ${{secrets.AWS_ECR_LOGIN_URI}}.dkr.ecr.${{ secrets.REGION_NAME }}.amazonaws.com/${{ secrets.ECR_REPOSITORY_NAME }}:latest