from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import WriterSerializer


class GigDescriptionView(APIView):

    def post(self, request):
        
        try:
            prompt = ''
            serializer = WriterSerializer(data=request.data)
            if serializer.is_valid():
                data = serializer.validated_data

                prompt = f'Write a Fiverr gig description for {data["service_type"]}.\nKeywords to include: {data["keywords"]}.'
                # print(prompt)
            else:
                print(serializer.errors)

        # Get OpenAI API key from secret manager
        # secrets = Secrets()
        # api_key = secrets.get_secret("openai")["api_key"]
        
        # Initialize OpenAI API client
        # openai.api_key = api_key
        
        # Generate gig description using ChatGPT
        # prompt = "Write a Fiverr gig description for a freelance graphic designer:"
        # response = openai.Completion.create(
        #     engine="davinci",
        #     prompt=prompt,
        #     max_tokens=150,
        #     n=1,
        #     stop=None,
        #     temperature=0.5,
        # )
        
        # gig_description = response["choices"][0]["text"]
        
            return Response({
                "data": serializer.data,
                "prompt": prompt
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                'error': serializer.error_messages,
                'error': str(e)
            })