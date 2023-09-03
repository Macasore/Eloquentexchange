"use client";

import Image from "next/image";
import Link from "next/link";
import { Revalia } from "next/font/google";
import * as z from "zod";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { Input } from "@/components/ui/input";
import { Checkbox } from "@/components/ui/checkbox";
import { Button } from "@/components/ui/button";
import { Apple, DirectRight } from "iconsax-react";
import { cn } from "@/lib/utils";
import { FcGoogle } from "react-icons/fc";

const formSchema = z
  .object({
    name: z.string().min(3),
    email: z.string().email(),
    password: z.string().min(8, {
      message: "Password must be at least 8 characters long",
    }),
    confirmPassword: z.string().min(8),
    terms: z.boolean({
      required_error: "Please agree to the terms and policy",
    }),
  })
  .refine((data) => data.password === data.confirmPassword, {
    message: "Passwords do not match",
    path: ["confirmPassword"],
  });

const font = Revalia({ subsets: ["latin"], weight: ["400"] });

const SignOutPage = () => {
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      name: "",
      email: "",
      password: "",
      confirmPassword: "",
      terms: false,
    },
  });

  const onSubmit = async (data: z.infer<typeof formSchema>) => {
    console.log(data);
  };

  const isLoading = form.formState.isSubmitting;

  return (
    <div className="flex justify-between pt-12 px-10 relative min-h-screen bg-[url('/rockets.svg')] bg-center bg-no-repeat bg-contain bg-fixed">
      <div className="flex flex-col items-start gap-y-8">
        <Image
          src="/coin.svg"
          alt="LiteCoin"
          width={80}
          height={80}
          className="ml-8"
        />
        <h1 className="text-5xl font-medium text-primary leading-snug">
          Sign up with <br /> Eloquent
        </h1>
        <p className="font-medium text-base">
          Already have an account? click here to{" "}
          <Link
            href="/sign-in"
            className="text-[#4168B7] dark:text-[#A77700] cursor-pointer hover:underline"
          >
            Sign in.
          </Link>
        </p>
      </div>
      <div className="flex flex-col space-y-8 w-[500px]">
        <h1 className="text-4xl font-semibold text-primary">Create Account</h1>
        <p className="text-muted-foreground">
          Enter your credentials to create an account.
        </p>
        <div>
          <Form {...form}>
            <form
              onSubmit={form.handleSubmit(onSubmit)}
              className="flex flex-col space-y-8"
            >
              <FormField
                control={form.control}
                name="name"
                render={({ field }) => (
                  <FormItem>
                    <FormControl>
                      <Input
                        disabled={isLoading}
                        placeholder="Full name"
                        className="border-t-0 font-medium text-primary rounded-none border-x-0 border-b-[#A77700] border-b-2 outline-none focus-visible:ring-0 focus-visible:ring-transparent"
                        {...field}
                      />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <FormField
                control={form.control}
                name="email"
                render={({ field }) => (
                  <FormItem>
                    <FormControl>
                      <Input
                        type="email"
                        disabled={isLoading}
                        placeholder="Email Address"
                        className="border-t-0 font-medium text-primary rounded-none border-x-0 border-b-[#A77700] border-b-2 outline-none focus-visible:ring-0 focus-visible:ring-transparent"
                        {...field}
                      />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <FormField
                control={form.control}
                name="password"
                render={({ field }) => (
                  <FormItem>
                    <FormControl>
                      <Input
                        disabled={isLoading}
                        placeholder="Password"
                        type="password"
                        className="border-t-0 font-medium text-primary rounded-none border-x-0 border-b-[#A77700] border-b-2 outline-none focus-visible:ring-0 focus-visible:ring-transparent"
                        {...field}
                      />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <FormField
                control={form.control}
                name="confirmPassword"
                render={({ field }) => (
                  <FormItem>
                    <FormControl>
                      <Input
                        disabled={isLoading}
                        placeholder="Confirm Password"
                        type="password"
                        className="border-t-0 font-medium text-primary rounded-none border-x-0 border-b-[#A77700] border-b-2 outline-none focus-visible:ring-0 focus-visible:ring-transparent"
                        {...field}
                      />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <div className="flex items-center w-full justify-end">
                <FormField
                  name="terms"
                  control={form.control}
                  render={({ field }) => (
                    <FormItem className="flex flex-col items-center space-x-3 space-y-0">
                      <div className="flex items-center space-x-3">
                        <FormControl>
                          <Checkbox
                            checked={field.value}
                            onCheckedChange={field.onChange}
                          />
                        </FormControl>
                        <FormLabel className="text-muted-foreground text-sm font-medium peer-disabled:cursor-not-allowed peer-disabled:opacity-70">
                          I agree to the{" "}
                          <Link href="/terms" className="underline">
                            terms & policy
                          </Link>
                        </FormLabel>
                      </div>
                      <FormMessage />
                    </FormItem>
                  )}
                />
              </div>
              <Button
                className="w-full text-white bg-[#4168B7] hover:bg-primary text-lg dark:bg-[#A77700] dark:hover:bg-primary hover:text-white dark:hover:text-black"
                variant="default"
              >
                Create Account
                <DirectRight className="w-5 h-5 ml-2" variant="Linear" />
              </Button>
            </form>
          </Form>
        </div>
        <p
          className={cn(
            "text-lg font-medium uppercase text-center",
            font.className
          )}
        >
          - or continue with
        </p>
        <div className="flex gap-x-8 justify-center">
          <div
            onClick={() => {}}
            className="w-10 h-10 rounded-lg border-[#A77700] border flex items-center justify-center cursor-pointer group"
          >
            <FcGoogle className="w-6 h-6 group-hover:scale-110" />
          </div>
          <div
            onClick={() => {}}
            className="w-10 h-10 rounded-lg border-[#A77700] border flex items-center justify-center cursor-pointer group "
          >
            <Apple variant="Bold" className="w-6 h-6 group-hover:scale-110" />
          </div>
        </div>
      </div>
    </div>
  );
};

export default SignOutPage;
